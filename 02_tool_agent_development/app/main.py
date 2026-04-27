from app.agent import run_agent
query=input("Enter query:").lower()
result=run_agent(query)
print("\nResult:",result)