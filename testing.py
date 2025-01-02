# def get_formatted_name(first, last,):
#     '''generate a neatly formatted name'''
#     f_name = first + ' ' + last
#     return f_name.title()

# rtrened=get_formatted_name('joe', 'doe')
# print(rtrened)


# #2.
# from names import get_formatted_name as gfn

# print ('enter q to quit.')
# while True:
#        fn=input('enter first name: ')
#        if fn == 'q':
#              break
#        ln=input('enter last name: ')
#        if ln=='q':
#              break
       
#        fnn = gfn(fn, ln)
#        print (fnn)
    

# #3. writing test cases - 
# import unittest as ut
# from names import get_formatted_name

# class NameTstCase(ut.TestCase):
#       ''' test for the function get formatted name'''

#       def test_first_last_name(self):
#             '''do names like joe doe work?'''
#             format_name = get_formatted_name('joe', 'doe')
#             # self.assertEqual(format_name, 'Joe Doe')
#             self.assertEqual(format_name, 'Joe Doe')

# ut.main()


# #4. passing a failing test - 

# def failed_test(f, l, m=''):
#       if m:
#             fname=f+' '+m+' '+l
#       else:
#             fname=f+' '+l
      
#       return fname.title()

# failed_test('joe', 'doe')



#5. adding new tests - 

# import unittest as ut
# from names import get_formatted_name as gfn

# class NameTestC(ut.TestCase):
#       '''testing for names with middle names'''
#       def test_first_name(self):
#             formated_n=gfn('joe', 'doe')
#             self.assertEqual(formated_n, 'Joe Doe')

#       def test_first_last_mid_name(self):
#             formated_n=gfn('joe', 'hope', 'doe')
#             self.assertEqual(formated_n, 'Joe Hope Doe')

# ut.main()


#6. testing a class - 

class AnonSurvey():
      '''collect anon answers to a survey question.'''

      def __init__(self, question):
            '''store a question and prepare to store responses'''
            self.question = question
            self.responses=[]

      def show_question(self):
            '''show survery questions'''
            print(question)

      def store_response(self, new_response):
            '''store a single response to the survey'''
            self.responses.append(new_response)

      def show_results(self):
            '''show all responses that were given'''
            print('Survey Results:')
            for response in self.responses:
                  print ('- ' + response)


# 7. writing a program from the above class

from testing import AnonSurvey

#define a question and make a survey
question='What is your mother language?'
my_survey= AnonSurvey(question)

# show the question, and store the responses to the question 
my_survey.show_question()
print('Enter q to quit\n')

while True:
      response=input('Language: ')
      if response == 'q':
            break
      my_survey.store_response(response.title())

#show the survey resutls
print('\n Thank you for taking the time to take the survey!\n')
print('Have a wonderful day!')
my_survey.show_results()



#testing the anon survery class
import unittest as ut
from testing import AnonSurvey

class TestAnonSurvey(ut.TestCase):
      '''test for class anonsurvey'''

      def test_store_single_response(self):
            '''test that single response is stored properly'''
            question='what language did you first learn to speak? '
            my_survey=AnonSurvey(question)
            my_survey.store_response('English')

            self.assertIn('English', my_survey.responses)

      def test_store_three_responses(self):
            '''test that three individual responses are stored properly'''
            question='what language do you speak presently?'
            my_survey=AnonSurvey(question)
            responses=['English', 'Hindi', 'Spanish']
            
            for response in responses:
                  my_survey.store_response(response)

            for response in responses:
                  self.assertIn(response, my_survey.responses)

ut.main()


