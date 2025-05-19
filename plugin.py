import json

class MedTermExplainer:
    def __init__(self, terms_file='terms.json'):
        with open(terms_file, 'r') as f:
            self.terms = json.load(f)

    def explain_term(self, term):
        term = term.lower().strip()
        return self.terms.get(term, "Sorry, I couldn't find a definition for that term.")

# Example usage
if __name__ == "__main__":
    explainer = MedTermExplainer()
    user_input = input("Enter a medical term: ")
    print(explainer.explain_term(user_input))
