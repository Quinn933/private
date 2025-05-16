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
# App-1
import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  debugShowCheckedModeBanner: false,
  home: AppOne(),
  ));

class AppOne extends StatefulWidget {
  @override
  _AppOneState createState() => _AppOneState();
}

class _AppOneState extends State<AppOne> {
  int counter = 0;

  void showSnack(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text("Snackbar pressed")),
    );
  }

  void increment() {
    setState(() {
      counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: Drawer(
        child: Center(child: Text("Drawer Menu")),
      ),
      appBar: AppBar(
        title: Text("STATEFUL"),
        actions: [
          IconButton(
            icon: Icon(Icons.notifications),
            onPressed: () => showSnack(context),
          ),
          PopupMenuButton<String>(
            onSelected: (value) {
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text("Selected: $value")),
              );
            },
            itemBuilder: (context) => [
              PopupMenuItem(value: "Option 1", child: Text("Option 1")),
              PopupMenuItem(value: "Option 2", child: Text("Option 2")),
            ],
          )
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            IconButton(
              iconSize: 60,
              icon: Icon(Icons.favorite),
              color: Colors.red,
              onPressed: increment,
            ),
            SizedBox(height: 10),
            Text(
              "You've pushed above button this many times",
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 20),
            Text(
              "$counter",
              style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}

# App-2
import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  debugShowCheckedModeBanner: false,
  home: AppTwo(),
  ));

class AppTwo extends StatefulWidget {
  @override
  _AppTwoState createState() => _AppTwoState();
}

class _AppTwoState extends State<AppTwo> {
  int value = 0;

  void increment() {
    setState(() {
      value++;
    });
  }

  void decrement() {
    setState(() {
      value--;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Plus Shape Counter")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                IconButton(
                  icon: Icon(Icons.add_circle),
                  color: Colors.green,
                  iconSize: 50,
                  onPressed: increment,
                ),
                SizedBox(width: 20),
                Text(
                  '$value',
                  style: TextStyle(fontSize: 40),
                ),
                SizedBox(width: 20),
                IconButton(
                  icon: Icon(Icons.remove_circle),
                  color: Colors.red,
                  iconSize: 50,
                  onPressed: decrement,
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}


# Assignment - 9
import 'package:flutter/material.dart';
import 'dart:math';

void main() => runApp(MaterialApp(
  debugShowCheckedModeBanner: false,
  home: ColorSizeChangerApp(),
));

class ColorSizeChangerApp extends StatefulWidget {
  @override
  _ColorSizeChangerAppState createState() => _ColorSizeChangerAppState();
}

class _ColorSizeChangerAppState extends State<ColorSizeChangerApp> {
  Color boxColor = Colors.blue;
  double boxSize = 100;

  void changeColor() {
    setState(() {
      boxColor = Color((Random().nextDouble() * 0xFFFFFF).toInt()).withOpacity(1.0);
    });
  }

  void increaseSize() {
    setState(() {
      boxSize += 20;
    });
  }

  void decreaseSize() {
    setState(() {
      if (boxSize > 40) boxSize -= 20;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Color & Size Changer")),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Center(
            child: AnimatedContainer(
              duration: Duration(milliseconds: 300),
              width: boxSize,
              height: boxSize,
              color: boxColor,
            ),
          ),
          SizedBox(height: 40),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              ElevatedButton(
                onPressed: changeColor,
                child: Text("Change Color"),
              ),
              ElevatedButton(
                onPressed: increaseSize,
                child: Text("Increase Size"),
              ),
              ElevatedButton(
                onPressed: decreaseSize,
                child: Text("Decrease Size"),
              ),
            ],
          ),
        ],
      ),
    );
  }
}


# Assignment - 10
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: LoginPage(),
  ));
}

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();

  void handleLogin() {
    String username = usernameController.text;
    String password = passwordController.text;

    print("Username: $username");
    print("Password: $password");

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text("Login pressed. Check console.")),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login Page")),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: usernameController,
              decoration: InputDecoration(
                labelText: "Username",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            TextField(
              controller: passwordController,
              obscureText: true, // hides password input
              decoration: InputDecoration(
                labelText: "Password",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 30),
            ElevatedButton(
              onPressed: handleLogin,
              child: Text("Login"),
            ),
          ],
        ),
      ),
    );
  }
}



# Assigmnent - 11
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: LoginPage(),
  ));
}

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();

  void handleLogin() {
    String username = usernameController.text.trim();
    String password = passwordController.text.trim();

    if (username == "Rishi" && password == "Pass001") {
      // Navigate to next screen
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => WelcomeScreen(username: username)),
      );
    } else {
      // Show snackbar for invalid credentials
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Invalid username or password")),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login Page")),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: usernameController,
              decoration: InputDecoration(
                labelText: "Username",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            TextField(
              controller: passwordController,
              obscureText: true,
              decoration: InputDecoration(
                labelText: "Password",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 30),
            ElevatedButton(
              onPressed: handleLogin,
              child: Text("Login"),
            ),
          ],
        ),
      ),
    );
  }
}

class WelcomeScreen extends StatelessWidget {
  final String username;

  WelcomeScreen({required this.username});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Welcome")),
      body: Center(
        child: Text(
          "Welcome, $username!",
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}
