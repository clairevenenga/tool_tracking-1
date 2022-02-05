import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(
    home: ToolTracking(),
  ));
}

class ToolTracking extends StatefulWidget {
  const ToolTracking({Key? key}) : super(key: key);

  @override
  _ToolTrackingState createState() => _ToolTrackingState();
}

class _ToolTrackingState extends State<ToolTracking> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('UGA College of Engineering'),
        backgroundColor: Colors.red,
        centerTitle: true,
        elevation: 0.0,
      ),
        bottomSheet: const Text('Please contact labsupport@uga.edu for additional support.',
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            textAlign: TextAlign.center,
        ),
        body: ListView(children: <Widget>[
          const Center(
            child:
              Text('Welcome to our tool service portal!',
                style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold)
              ),
          ),
          const SizedBox(
            height: 50.0,
          ),
          const Center(
            child:
            Text('Click on a tool to learn more about its description, location, availability, and mobility.',
                style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold)
            ),
          ),
          const SizedBox(
            height: 50.0,
          ),
          const Center(
              child:
              Text('Tool Catalog',
                style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold),
              ),
          ),
          const SizedBox(
            height: 10.0,
          ),
          DataTable(
            columns: const [
              DataColumn(label: Text(
                  'TOOL NAME',
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)
              )),
              DataColumn(label: Text(
                  'TOOL ID',
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)
              )),
              DataColumn(label: Text(
                  'AVAILABILITY',
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)
              )),
              DataColumn(label: Text(
                  'MOBILITY',
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)
              )),
            ],
            rows: const [
              DataRow(cells: [
                DataCell(Text('Tool A')),
                DataCell(Text('A1')),
                DataCell(Text('Available')),
                DataCell(Text('Stationary')),
              ]),
              DataRow(cells: [
                DataCell(Text('Tool A')),
                DataCell(Text('A1')),
                DataCell(Text('Unavailable')),
                DataCell(Text('Non-stationary')),
              ]),
              DataRow(cells: [
                DataCell(Text('Tool C')),
                DataCell(Text('C1')),
                DataCell(Text('Unavailable')),
                DataCell(Text('Stationary')),
              ]),
            ],
          ),
        ])
    );
  }
}

