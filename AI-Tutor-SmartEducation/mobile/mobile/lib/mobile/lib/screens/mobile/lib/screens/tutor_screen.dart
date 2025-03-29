import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class TutorScreen extends StatefulWidget {
  @override
  _TutorScreenState createState() => _TutorScreenState();
}

class _TutorScreenState extends State<TutorScreen> {
  final TextEditingController _controller = TextEditingController();
  String _prediction = "";

  Future<void> _predict() async {
    final response = await http.post(
      Uri.parse('http://127.0.0.1:8000/predict/'),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"features": _controller.text.split(",").map(double.parse).toList()}),
    );

    final data = jsonDecode(response.body);
    setState(() {
      _prediction = data["prediction"].toString();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("AI Tutor")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              decoration: InputDecoration(labelText: "Enter numbers (comma-separated)"),
            ),
            SizedBox(height: 20),
            ElevatedButton(child: Text("Predict"), onPressed: _predict),
            SizedBox(height: 20),
            Text("Prediction: $_prediction"),
          ],
        ),
      ),
    );
  }
}
