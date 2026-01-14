#Question1:Message counter(Immutable parameters)
#This function counts how many times a message is paassed.
#It demonstrates the concept of immutable parameters in python.
#It demonstrates the concept of immutable parameters in python.
#The'count'variable is an integer (immutable), so each function call 
#starts with the default value(0) and does not retain previous changes.
def count_message(msg, count=0):
    #Increment the count each time the function is called
    count += 1
    #print the message along with the current count.
    print(f"Message: {msg} | Count: {count}")
    #Return the updated count value
    return count

# Test calls
#Each time we call the function,count resets to 0(becaz int are immutable)
count1 = count_message("harish")
#output:message:harish|count:1
count2 = count_message("hello")
#output:message:hello|count:1
count3 = count_message("seeyou")
#output:message:seeyou|count:1
#Explanation:
#Even though we called the function multiple times , 'count' does not remember previous values.
#this happens because integers are immutable and default parameters are reinitialized each call.
