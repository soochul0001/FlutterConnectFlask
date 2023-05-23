import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Flutter & Flask 연동'),
        ),
        body: Center(
          child: ElevatedButton(
            onPressed: () {
              sendData();
            },
            child: Text('데이터 전송'),
          ),
        ),
      ),
    );
  }

  void sendData() async {
    var url = 'http://localhost:5000/api/data'; // Flask 서버 주소
    var data = {'message': 'Hello from Flutter!'};

    var response = await http.post(
      Uri.parse(url),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(data),
    );

    if (response.statusCode == 200) {
      var result = jsonDecode(response.body);
      print(result['message']);
    } else {
      print('Error: ${response.statusCode}');
    }
  }
}
