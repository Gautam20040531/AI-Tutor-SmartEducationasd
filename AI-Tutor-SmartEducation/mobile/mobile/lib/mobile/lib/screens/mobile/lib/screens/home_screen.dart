import 'package:flutter/material.dart';
import 'tutor_screen.dart';
import 'chatbot_screen.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("AI Tutor Smart Education")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text("AI Tutor"),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context) => TutorScreen()));
              },
            ),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text("AI Chatbot"),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context) => ChatbotScreen()));
              },
            ),
          ],
        ),
      ),
    );
  }
}
