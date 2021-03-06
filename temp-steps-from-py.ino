const byte temps[] ={20,
21,
22,
23,
24,
25,
26,
26,
27,
28,
29,
30,
31,
32,
32,
33,
34,
35,
36,
37,
38,
38,
39,
40,
41,
42,
43,
44,
44,
45,
46,
47,
48,
49,
50,
50,
51,
52,
53,
54,
55,
56,
56,
57,
58,
59,
60,
61,
62,
62,
63,
64,
65,
66,
67,
68,
68,
69,
70,
71,
72,
73,
74,
74,
75,
76,
77,
78,
79,
80,
80,
81,
82,
83,
84,
85,
86,
86,
87,
88,
89,
90,
91,
92,
92,
93,
94,
95,
96,
97,
98,
98,
99,
100,
101,
102,
103,
104,
104,
105,
106,
107,
108,
109,
110,
110,
111,
112,
113,
114,
115,
116,
116,
117,
118,
119,
120,
121,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
122,
121,
120,
119,
118,
117,
116,
116,
115,
114,
113,
112,
111,
110,
110,
109,
108,
107,
106,
105,
104,
104,
103,
102,
101,
100,
99,
98,
98,
97,
96,
95,
94,
93,
92,
92,
91,
90,
89,
88,
87,
86,
86,
85,
84,
83,
82,
81,
80,
80,
79,
78,
77,
76,
75,
74,
74,
73,
72,
71,
70,
69,
68,
68,
67,
66,
65,
64,
63,
62,
62,
61,
60,
59,
58,
57,
56,
56,
55,
54,
53,
52,
51,
50,
50,
49,
48,
47,
46,
45,
44,
44,
43,
42,
41,
40,
39,
38,
38,
37,
36,
35,
34,
33,
32,
32,
31,
30,
29,
28,
27,
26,
26,
25,
24,
23,
22,
21,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20,
20};
const int ntemps = 360;
const float dt = .1;
// end py

// the pin for the output
const int analogOutPin = 9;
// The analog value to be output to the pin. Initialized to 0
int outputValue = 0;

// converts the value to a temp to be sent to the serial monitor
float bin_to_temp(byte bin){
    float fbin = bin;
    float temp = (fbin * 50.0) / 255.0;
    return temp;
  
}

void setup() {
  // set up serial communication
  Serial.begin(9600);
}

void loop() {
  // time between ramps in ms
  float delay_time = 1000*dt;
  // iterate through temps
  for (int i=0; i<ntemps; i++){
    byte outputValue = temps[i];
    // make a debugging display
    float temp = bin_to_temp(outputValue);
    Serial.print(temp);
    Serial.print("\t");
    Serial.println(outputValue);
    // set the pin to the correct value for temp
    analogWrite(analogOutPin, outputValue);
    // delay for dt
    delay(delay_time);
  }
}

