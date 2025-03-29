import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class ChatbotScreen extends StatefulWidget {
  @override
  _ChatbotScreenState createState() => _ChatbotScreenState();
}

class _ChatbotScreenState extends State<ChatbotScreen> {
  final TextEditingController _controller = TextEditingController();
  String _response = "";

  Future<void> _sendMessage() async {
    final response = await http.post(
      Uri.parse('http://127.0.0.1:8000/chat/'),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"message": _controller.text}),
    );

    final data = jsonDecode(response.body);
    setState(() {
      _response = data["response"];
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("AI Chatbot")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              decoration: InputDecoration(labelText: "Ask something..."),
            ),
            SizedBox(height: 20),
            ElevatedButton(child: Text("Send"), onPressed: _sendMessage),
            SizedBox(height: 20),
            Text("Bot: $_response"),
          ],
        ),
      ),
    );
  }
}
