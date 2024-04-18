const int redNorth = 4;
const int yellowNorth = 3;
const int greenNorth = 2;

const int redSouth = 7;
const int yellowSouth = 6;
const int greenSouth = 5;

void setup() {
  Serial.begin(9600);

  pinMode(redNorth, OUTPUT);
  pinMode(yellowNorth, OUTPUT);
  pinMode(greenNorth, OUTPUT);

  pinMode(redSouth, OUTPUT);
  pinMode(yellowSouth, OUTPUT);
  pinMode(greenSouth, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readString();

    if (message.equals("road1 go")) {
      // Implement the actions for road1
      digitalWrite(redNorth, LOW);
      digitalWrite(yellowNorth, LOW);
      digitalWrite(greenNorth, HIGH);
      delay(5000);  // Green for road1 for 5 seconds

      // Reset lights for road1
      digitalWrite(redNorth, LOW);
      digitalWrite(yellowNorth, HIGH);
      digitalWrite(greenNorth, LOW);
      delay(3000);  // Yellow for road1 for 3 seconds

      digitalWrite(redNorth, HIGH);
      digitalWrite(yellowNorth, LOW);
      digitalWrite(greenNorth, LOW);
      delay(3000);  // Red for road1 for 3 seconds

    } else if (message.equals("road2 go")) {
      // Implement the actions for road2
      digitalWrite(redSouth, LOW);
      digitalWrite(yellowSouth, LOW);
      digitalWrite(greenSouth, HIGH);
      delay(5000);  // Green for road2 for 5 seconds

      // Reset lights for road2
      digitalWrite(redSouth, LOW);
      digitalWrite(yellowSouth, HIGH);
      digitalWrite(greenSouth, LOW);
      delay(3000);  // Yellow for road2 for 3 seconds

      digitalWrite(redSouth, HIGH);
      digitalWrite(yellowSouth, LOW);
      digitalWrite(greenSouth, LOW);
      delay(3000);  // Red for road2 for 3 seconds
    }
  }
}
