
%% Part A
Ku = 100;
Ti = 5.625;
b = 40;
m = 400; %Test for values between 50 and 400 for worst case scenario
%Convert the PI transfer function to state space
num1 = [Ku*Ti Ku]; 
den1 = [Ti 0]; 
[A,B,C,D] = tf2ss(num1,den1);
%% Part B
Kp = 0.2312;
Td = 6.7661;
Te = 1.6892;
%Convert the PD transfer function to state space
%num = [Kp*(Te+Td) Kp]; den = [Te 1]; [A,B,C,D] = tf2ss(num,den);
%% Part C
Init = -75;