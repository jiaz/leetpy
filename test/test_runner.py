import inspect
import os.path


myPath = os.path.realpath(__file__)


class ParamsDef(object):
    def __init__(self, params=[], result=None):
        self.params = params
        self.result = result


def loadCases(id):
    caseFiles = ['%s_Small.txt' % id, '%s_Large.txt' % id]
    cases = []
    for caseFile in caseFiles:
        casePath = os.path.join(os.path.dirname(myPath), 'CaseData', caseFile)
        with open(casePath) as f:
            for line in f.readlines():
                params, res = line.split("\t")[:2]
                params = params.split(', ')
                params.append(res)
                cases.append(params)
    return cases


def parseParams(doc):
    params = map(lambda x: x.strip(), doc.strip().split('\n'))
    paramsDef = ParamsDef()
    for param in params:
        if param.find(':type') != -1:
            _, paramName, paramType = param.split(' ')
            paramName = paramName[:-1]
            paramsDef.params.append({'name': paramName, 'type': paramType})
        if param.find(':rtype') != -1:
            _, resultType = param.split(' ')
            paramsDef.result = {'type': resultType}
    return paramsDef


def asList(s):
    return eval(s)


def toFloatStr(v):
    return '%.5f' % v


def deserialize(s, paramType):
    if paramType.find('List') != -1:
        return asList(s)
    elif paramType == 'str':
        return eval(s)
    elif paramType == 'int':
        return eval(s)
    else:
        raise RuntimeError('not supported paramType: %s' % paramType)


def serialize(v, resultType):
    if resultType.find('float') != -1:
        return toFloatStr(v)
    elif resultType == 'str':
        return '"%s"' % v
    else:
        raise RuntimeError('not supported resultType: %s' % resultType)


def execute(target, paramsDef, case):
    kwargs = {}

    for i in range(len(paramsDef.params)):
        paramName = paramsDef.params[i]['name']
        paramType = paramsDef.params[i]['type']
        kwargs[paramName] = deserialize(case[i], paramType)

    result = target.__call__(**kwargs)

    if paramsDef.result is not None:
        resultType = paramsDef.result['type']
        serializedResult = serialize(result, resultType)
        assert serializedResult == case[-1], 'case %s' % ', '.join(case)


def run(s, id):
    # find impl
    members = inspect.getmembers(s, predicate=inspect.ismethod)
    target = None
    for m in members:
        if m[1].__doc__ and m[1].__doc__.find(':type') != -1:
            target = m[1]
            break

    if target is None:
        raise RuntimeError('no test target found on the solution object')

    paramsDef = parseParams(target.__doc__)

    cases = loadCases(id)

    # execute cases
    for case in cases:
        execute(target, paramsDef, case)
