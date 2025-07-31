from hstest import dynamic_test, StageTest, CheckResult, TestedProgram
import re


class Test(StageTest):

    responses = []

    @dynamic_test(time_limit=60000, data=list(range(3)))
    def test1(self, runs):
        program = TestedProgram()
        output = program.start().strip()

        #output = program.execute()

        # Check if response is different from the previous one
        if output in self.responses:
            return CheckResult.wrong("The response is the same as the previous one. "
                                     "It should be different each time.")
        self.responses.append(output)

        return CheckResult.correct()


if __name__ == '__main__':
    Test('main').run_tests()