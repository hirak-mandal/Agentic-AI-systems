from app.agent import run_agent
query=input("Enter your query: ")
result=run_agent(query)
print("\nFinal Result:",result)