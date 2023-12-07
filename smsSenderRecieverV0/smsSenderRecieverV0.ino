#include <GSM.h>

#define PINNUMBER "0000"

GSM gsmAccess;
GSM_SMS sms;

char remoteNumber[20] = "0650874313";

void setup() {
  Serial.begin(9600);
  Serial.println("SMS Messages Sender");

  boolean notConnected = true;

  while (notConnected) {
    if (gsmAccess.begin(PINNUMBER) == GSM_READY)
      notConnected = false;
    else {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
}

void loop() {
  if (Serial.available() > 0) {
    String receivedMessage = Serial.readStringUntil('\n');
    Serial.print("Received Message: ");
    Serial.println(receivedMessage);
    sendSMS(receivedMessage);
  }

  checkAndReadSMS();
}

void sendSMS(String message) {
  // Extract phone number and message from the received string
  int separatorIndex = message.indexOf(':');
  if (separatorIndex == -1) {
    Serial.println("Invalid message format. Use 'phone_number:message'");
    return;
  }

  String phone_number = message.substring(0, separatorIndex);
  String sms_message = message.substring(separatorIndex + 1);

  Serial.print("Message to mobile number: ");
  Serial.println(phone_number);

  Serial.println("SENDING");
  Serial.println("Message:");
  Serial.println(sms_message);

  if (sms.beginSMS(phone_number.c_str())) {
    sms.print(sms_message);
    if (sms.endSMS()) {
      Serial.println("SMS sent successfully");
    } else {
      Serial.println("Failed to send SMS");
    }
  } else {
    Serial.println("Failed to begin SMS");
  }

  Serial.println("\nCOMPLETE!\n");
}

void checkAndReadSMS() {
  // Check if there are any SMS messages available
  if (sms.available()) {
    Serial.println("Reading SMS...");

    // Get the message details
    char c;
    String message = "";
    while ((c = sms.read()) != '\0') {
      message += c;
    }

    Serial.print("Received SMS: ");
    Serial.println(message);

    // You can add your processing logic for the received SMS here

    // Delete the received SMS from the SIM card
    sms.flush();

    Serial.println("SMS read complete\n");
  }
}
