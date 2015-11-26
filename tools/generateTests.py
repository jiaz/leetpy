import os
import os.path

myPath = os.path.realpath(__file__)

for dirname, dirnames, filenames in os.walk(os.path.join(os.path.dirname(myPath), '../leetcode')):
    for f in filenames:
        if f != '__init__.py' and f.find('pyc') == -1:
            testFile = 'test_%s' % f
            testFilePath = os.path.normpath(os.path.join(os.path.dirname(myPath), '../test', testFile))
            if not os.path.isfile(testFilePath):
                print testFilePath
                with open(testFilePath, 'w') as fd:
                    fd.write('from leetcode.%s import Solution\n' % f[:-3])
                    fd.write('from test_runner import run\n')
                    fd.write('\n')
                    fd.write('\n')
                    fd.write('def %s():\n' % testFile[:-3])
                    fd.write('    s = Solution()\n')
                    fd.write('    run(s, \'%s\')\n' % f[:4])

