import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(AITutorApp());
}

class AITutorApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'AI Tutor Smart Education',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomeScreen(),
    );
  }
}
