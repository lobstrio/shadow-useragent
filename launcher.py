from core import UserAgentCollector

user_agent_collector = UserAgentCollector()
# user_agent_collector.update()
user_agent_collector._update()
#random = user_agent_collector.random()
#print(random)
print(user_agent_collector.firefox)
print(user_agent_collector.chrome)
# print(user_agent_collector.random)
# print(user_agent_collector.display_uas())
