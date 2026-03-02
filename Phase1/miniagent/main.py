from agents.searchAgent import SearchAgent
from agents.calculatorAgent import CalculatorAgent
from router import Router
def main():
    agents = [
        CalculatorAgent("MathSolver"),
        SearchAgent("WebSearch")
    ]
    router = Router(agents)
    while True:
        query = input("Enter query (or type 'exit'): ")
        if query.lower() == "exit":
            break
        response = router.route(query)
        print(response)
if __name__ == "__main__":
    main()