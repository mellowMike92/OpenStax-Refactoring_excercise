
class Questions:

    def __init__(self):
        # self.pop_questions = []
        # self.science_questions = []
        # self.sports_questions = []
        # self.rock_questions = []

        self.types_of_questions = {
            'Pop': [],
            'Sports': [],
            'Science': [],
            'Rock': []
        }
        self.number_of_questions = 50

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for question_number in range(self.number_of_questions):
            # self.pop_questions.append(self._create_pop_question(question_number))
            # self.science_questions.append(self._create_science_question(question_number))
            # self.sports_questions.append(self._create_sports_question(question_number))
            # self.rock_questions.append(self._create_rock_question(question_number))

            for question_type, question_statement in self.types_of_questions.items():

                self.types_of_questions[question_type].append(create_question_type(question_type, question_number))


def create_question_type(question_type, question_number):
    return str(question_type) + " Question %s" % question_number
    #
    # @staticmethod
    # def _create_rock_question(index):
    #     return "Rock Question %s" % index
    #
    # @staticmethod
    # def _create_sports_question(index):
    #     return "Sports Question %s" % index
    #
    # @staticmethod
    # def _create_science_question(index):
    #     return "Science Question %s" % index
    #
    # @staticmethod
    # def _create_pop_question(index):
    #     return "Pop Question %s" % index
