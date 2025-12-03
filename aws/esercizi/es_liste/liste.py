
server = ["web01", "db01", "cache01"]
print(server) 
print("*"*30)
server.append("backup01")

print(server)
print("*"*30)
server.insert(0,"proxy01")

print(server)
print("*"*30)
server.pop(3)

print(server)

print("*"*30)

print(print(len(server)))
print("*"*30)


