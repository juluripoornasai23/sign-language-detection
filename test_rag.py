from rag_model.rag_pipelines import ask

while True:

    q = input("Ask : ")

    if q.lower() == "exit":
        break

    print()
    print(ask(q))
    print()