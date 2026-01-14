def count_message(msg, count=0):
    count += 1
    print(f"Message: {msg} | Count: {count}")
    return count

# Test calls
count1 = count_message("heya")
count2 = count_message("hello")
