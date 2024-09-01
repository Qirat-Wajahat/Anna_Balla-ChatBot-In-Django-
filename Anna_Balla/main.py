from .chatBot import chatbot
import webbrowser as wb
import datetime as dt

def main(query):
    print(query)

    if query:
        if 'open' in query.lower():
            if "youtube" in query.lower():
                wb.open("https://www.youtube.com")
                print("Opening YouTube...")
                return "Opening YouTube..."

        elif "time" in query.lower():
            current_time = dt.datetime.now().strftime("%H:%M:%S")
            print(f"The current time is {current_time}.")
            return f"The current time is {current_time}."

        elif "ok stop" in query.lower():
            print("Goodbye! Have a great day.")
            return "Goodbye! Have a great day."

        # Call the AIML API for other queries
        else:
            content = chatbot(query)
            return content

    return "Sorry, I didn't understand that."
