
class Questions:

    def __init__(self):
        self.types_of_questions = {
            'Pop': [],
            'Sports': [],
            'Science': [],
            'Rock': []
        }
        self.number_of_questions = 50
        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        self._initialize_questions()

    def _initialize_questions(self):
        for question_number in range(self.number_of_questions):
            for question_type, question_statement in self.types_of_questions.items():
                self._create_question_statements(question_number, question_type)

    def _create_question_statements(self, question_number, question_type):
        self.types_of_questions[question_type].append(str(question_type) + " Question %s" % question_number)

