import unittest#########报错找不到原因
from Survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        self.question='what language did you first learn to speak?'
        self.my_survey=AnonymousSurvey(self.question)
        self.my_survey.store_reponse('English')
        self.assertIn('English',self.my_survey.responses)

    # def test_store_three_responses(self):
    #     question='what language did you first learn to speak?'
    #     my_survey=AnonymousSurvey(question)
    #     responses=['english','chinese','spanish']
    #     for response in responses:
    #         my_survey.store_reponse(response)
    #     for response in responses:
    #         self.assertIn(response,my_survey.responses)

if __name__=='__main__':
    unittest.main()