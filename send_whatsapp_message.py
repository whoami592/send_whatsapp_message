import pywhatkit
import time

# Function to send a WhatsApp message to a phone number
def send_whatsapp_message(phone_number, message):
    try:
        # Send message to the specified phone number
        # Format phone number as "+countrycodephonenumber" (e.g., "+923118209360")
        pywhatkit.sendwhatmsg(phone_number, message, time.localtime().tm_hour, time.localtime().tm_min + 1)
        print(f"Message sent successfully to {phone_number}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to send a WhatsApp message to a group
def send_whatsapp_group_message(group_id, message):
    try:
        # Send message to the specified group ID
        pywhatkit.sendwhatmsg_to_group(group_id, message, time.localtime().tm_hour, time.localtime().tm_min + 1)
        print(f"Message sent successfully to group {group_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with the recipient's phone number in international format
    phone_number = "+923409777222"  # Example phone number
    message = "i am pakistani ethical hacker mr sabaz ali khan!"
    
    # Send message to individual
    send_whatsapp_message(phone_number, message)
    
    # Replace with the WhatsApp group ID
    group_id = "GROUP_ID_HERE"  # Example group ID
    group_message = "Hello group, this is a test message sent via Python!"
    
    # Send message to group
    send_whatsapp_group_message(group_id, group_message)