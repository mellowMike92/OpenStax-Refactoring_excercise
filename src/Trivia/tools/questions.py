from src.Trivia.tools.players import Players


class Questions(Players):

    def __init__(self):
        """ Initializes the class by inheriting from the Players base class.
        Creates a dictionary mapping the question categories as keys to empty lists as values. """
        super().__init__()
        self.question_categories = {
            'Pop': [],
            'Sports': [],
            'Science': [],
            'Rock': []
        }
        self.number_of_questions = 50  # Number of questions can now be modified from client side.
        self.is_getting_out_of_penalty_box = False
        self._initialize_questions()

    def _initialize_questions(self):
        """ Nested loop of number and categories of questions to quickly construct the question statements. """
        for question_number in range(self.number_of_questions):
            for question_type, question_statement in self.question_categories.items():
                self._create_question_statements(question_number, question_type)

    def _create_question_statements(self, question_number, question_type):
        """ Constructs the question statements using the keys from the categories_of_questions dictionary
        and the question number from the range(number_of_questions) iteration. """
        self.question_categories[question_type].append(str(question_type) + " Question %s" % question_number)



