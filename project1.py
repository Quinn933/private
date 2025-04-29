import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: BMICalculator(),
  ));
}

class BMICalculator extends StatefulWidget {
  @override
  _BMICalculatorState createState() => _BMICalculatorState();
}

class _BMICalculatorState extends State<BMICalculator> {
  TextEditingController heightController = TextEditingController();
  TextEditingController weightController = TextEditingController();
  String result = "";

  void calculateBMI() {
    double height = double.parse(heightController.text);
    double weight = double.parse(weightController.text);
    double bmi = weight / (height * height);

    String category = "";
    if (bmi < 18.5) {
      category = "Underweight";
    } else if (bmi < 24.9) {
      category = "Normal weight";
    } else if (bmi < 29.9) {
      category = "Overweight";
    } else {
      category = "Obesity";
    }

    setState(() {
      result = "Your BMI is ${bmi.toStringAsFixed(2)}\n($category)";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('BMI Calculator')),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: [
            TextField(
              controller: heightController,
              decoration: InputDecoration(labelText: "Height (m)"),
              keyboardType: TextInputType.number,
            ),
            TextField(
              controller: weightController,
              decoration: InputDecoration(labelText: "Weight (kg)"),
              keyboardType: TextInputType.number,
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: calculateBMI,
              child: Text("Calculate"),
            ),
            SizedBox(height: 20),
            Text(result, style: TextStyle(fontSize: 22)),
          ],
        ),
      ),
    );
  }
}
