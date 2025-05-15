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


# Assignment - 5
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: MyHomePage(),
  ));
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          title: Text("TabBar R/C"),
          backgroundColor: Colors.transparent,
          elevation: 0,
          flexibleSpace: Image.network(
            'https://images.unsplash.com/photo-1503264116251-35a269479413',
            fit: BoxFit.cover,
          ),
          leading: IconButton(
            icon: Icon(Icons.menu, color: Colors.white),
            onPressed: () {},
          ),
          actions: [
            IconButton(
              icon: Icon(Icons.search, color: Colors.white),
              onPressed: () {},
            ),
            IconButton(
              icon: Icon(Icons.more_vert, color: Colors.white),
              onPressed: () {},
            ),
          ],
          bottom: TabBar(
            indicatorColor: Colors.white,
            labelColor: Colors.white,
            unselectedLabelColor: Colors.black,
            tabs: [
              Tab(text: "Row"),
              Tab(text: "Column"),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            // Row Tab with unique image
            Container(
              decoration: BoxDecoration(
                image: DecorationImage(
                  image: NetworkImage(
                    'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0',
                  ),
                  fit: BoxFit.cover,
                ),
              ),
              child: Center(
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    buildBox(),
                    buildBox(),
                    buildBox(),
                  ],
                ),
              ),
            ),
            // Column Tab with different image
            Container(
              decoration: BoxDecoration(
                image: DecorationImage(
                  image: NetworkImage(
                    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759?auto=format&fit=crop&w=800&q=80',
                  ),
                  fit: BoxFit.cover,
                ),
              ),
              child: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    buildBox(),
                    buildBox(),
                    buildBox(),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget buildBox() {
    return Container(
      margin: EdgeInsets.all(10),
      width: 100,
      height: 100,
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [Colors.yellow, Colors.red],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(15),
        boxShadow: [
          BoxShadow(
            color: Colors.black26,
            blurRadius: 5,
            spreadRadius: 2,
          ),
        ],
      ),
      child: Center(
        child: Text(
          "I'm a box",
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
      ),
    );
  }
}


# Assignment - 6
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: MyHomePage(),
  ));
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          title: Text("TabBar R/C"),
          backgroundColor: Colors.transparent,
          elevation: 0,
          flexibleSpace: Image.network(
            'https://images.unsplash.com/photo-1503264116251-35a269479413',
            fit: BoxFit.cover,
          ),
          leading: IconButton(
            icon: Icon(Icons.menu, color: Colors.white),
            onPressed: () {},
          ),
          actions: [
            IconButton(
              icon: Icon(Icons.search, color: Colors.white),
              onPressed: () {},
            ),
            IconButton(
              icon: Icon(Icons.more_vert, color: Colors.white),
              onPressed: () {},
            ),
          ],
          bottom: TabBar(
            indicatorColor: Colors.white,
            labelColor: Colors.white,
            unselectedLabelColor: Colors.black,
            tabs: [
              Tab(text: "Row"),
              Tab(text: "Column"),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            // Row Tab with background
            Container(
              decoration: BoxDecoration(
                image: DecorationImage(
                  image: NetworkImage(
                    'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0',
                  ),
                  fit: BoxFit.cover,
                ),
              ),
              child: Center(
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    buildBox(context),
                    buildBox(context),
                    buildBox(context),
                  ],
                ),
              ),
            ),
            // Column Tab with background
            Container(
              decoration: BoxDecoration(
                image: DecorationImage(
                  image: NetworkImage(
                    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759?auto=format&fit=crop&w=800&q=80',
                  ),
                  fit: BoxFit.cover,
                ),
              ),
              child: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    buildBox(context),
                    buildBox(context),
                    buildBox(context),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget buildBox(BuildContext context) {
    return Container(
      margin: EdgeInsets.all(10),
      width: 100,
      height: 100,
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [Colors.yellow, Colors.red],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(15),
        boxShadow: [
          BoxShadow(
            color: Colors.black26,
            blurRadius: 5,
            spreadRadius: 2,
          ),
        ],
      ),
      child: Center(
        child: TextButton(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => SecondPage()),
            );
          },
          style: TextButton.styleFrom(
            backgroundColor: Colors.transparent, // Let gradient show
            foregroundColor: Colors.white,
          ),
          child: Text("Open"),
        ),
      ),
    );
  }
}

// ✅ New Page Widget
class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Second Page")),
      body: Center(
        child: Text("Welcome to a new screen!",
            style: TextStyle(fontSize: 24)),
      ),
    );
  }
}


# Assignment - 7
