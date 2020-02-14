%Lab Assessment 2
%%
clear all;
close all;
clc;
%Question 1 
%%%%%%%%%REMEMBER TO RENAME IMAGE 3 TIMES FOR THE DIFFERENT IMAGES
Imgname = 'disney.jpg'; % Loading the chosen image into Matlab
Image = imread(Imgname); % Reads the images data and loads it into the variable 'Image'
Gray = rgb2gray(Image); % Converts the image from colour to gray by converting the RGB values to grayscale values
figure(1) % New figure to display original and gray image on the same figure hence the use of subplot
subplot(1,2,1); imshow(Image), title('Original Image') % Display the original image with a title stating it as the original image
subplot(1,2,2); imshow(Gray), title('Gray Image') % Display the gray image with a title stating it as the gray image
[J,K] = size(Gray); % Defines the matrix 'Gray' where 'J' and 'K' are the row and column vectors that are returned as seperate variables
NoP = 1:1:256; % Y-axis values (Number of Pixels)
Int = 0:1:255; % X-axis values (Intensity)
Count = 0; % Setting an initial value
for a = 0:255 % First for loop: Checking the picture 255 times for all of the pixel values('a')
    for j = 1:J % Second for loop: Checking the pixel values row by row
        for k = 1:K % Third for loop: checking the pixel values column by column
            if Gray(j,k) == a % Check if the pixel value in the image matches the 'a' value
            Count = Count + 1; % If the values match the counter increments by 1
            end % Ending the if statement
        end % Ending the third for loop
    end % Ending the second for loop
    NoP(a+1) = Count; % Save the 'Count' values in an element
    Count = 0; % Clear the 'Count' so it is ready to read the next values
end % Ending the first for loop
figure(2) % New figure to display the following information
plot(Int,NoP); % Plots the intensity against the number of pixels
grid on % Displays a grid on the plot
title('Histogram of Gray Image'); % Labelling the title of the graph as "Histogram"
xlim([0;255]); % Limiting the x-axis range between 0 and 255 
xlabel('Intensity'); % Labelling the x-axis as "Intensity"
ylabel('Number of Pixels'); % Labelling the y-axis as "Number of Pixels"
%%
%Question 2
%Part a
Imin = 110; % Minimum intensity value of the original image (my chosen value)
Imax = 210;% Maximum intensity value of the original image (my chosen value)
Nmin = 0; % Setting the desired intensity minimum intensity value
Nmax = 255; % Setting the desired maximum intensity value
a62 = imread('a62.tif');
I = rgb2gray(a62); % Loading the image 'a62' into Matlab and converting it to grayscale
Isize = size(I); % Returns the two-element row vector, in this case a x-by-y matrix I
N = I; % Copying the loaded image into a new variable so that the new variable can be enhanced while keeping a copy of the original
for x = 1:Isize(1) % First for loop: reading all values from 1 to 381, where Isize(1)=381 (Isize(1) is the first element when the image is loaded displaying its height)
    for y = 1:Isize(2) % Second for loop: reading all values from 1 to 512, where Isize(1)=512 (Isize(2) is the second element when the image is loaded displaying its width)
        N(x,y) = ((I(x,y)-Imin)*((Nmax-Nmin)/(Imax-Imin)))+Nmin; % Equation that calculates the normalised intensity value for (x,y)
    end % Ending the second for loop
end % Ending the first for loop
figure(3) % New figure to display gray image and enhanced contrast of the image on the same figure hence the use of subplot
subplot(1,2,1); imshow(I), title('Gray Image')
subplot(1,2,2); imshow(N), title('Enhanced Contrast of Image')
%Part b
Imgname = 'a62.tif'; % Loading the chosen image ('a62.tif') into Matlab
Image = imread(Imgname); % Reads the images data and loads it into the variable 'Image'
Gray = rgb2gray(Image); % Converts the image from colour to gray by converting the RGB values to grayscale values
figure(4) % New figure to display original and gray image on the same figure hence the use of subplot
subplot(1,2,1); imshow(Image), title('Original Image: a62') % Display the original image with a title stating it as the original image
subplot(1,2,2); imshow(Gray), title('Gray Image: a62') % Display the gray image with a title stating it as the gray image
[J,K] = size(Gray); % Defines the matrix 'Gray' where 'J' and 'K' are the row and column vectors that are returned as seperate variables
NoP = 1:1:256; % Y-axis values (Number of Pixels)
Int = 0:1:255; % X-axis values (Intensity)
Count = 0; % Setting an initial value
for a = 0:255 % First for loop: Checking the picture 255 times for all of the pixel values('a')
    for j = 1:J % Second for loop: Checking the pixel values row by row
        for k = 1:K % Third for loop: checking the pixel values column by column
            if Gray(j,k) == a % Check if the pixel value in the image matches the 'a' value
            Count = Count + 1; % If the values match the counter increments by 1
            end % Ending the if statement
        end % Ending the third for loop
    end % Ending the second for loop
    NoP(a+1) = Count; % Save the 'Count' values in an element
    Count = 0; % Clear the 'Count' so it is ready to read the next values
end % Ending the first for loop
figure(5) % New figure to display the following information
plot(Int,NoP); % Plots the intensity against the number of pixels
grid on % Displays a grid on the plot
title('Histogram of Gray Image: a62'); % Labelling the title of the graph as "Histogram"
xlim([0;255]); % Limiting the x-axis range between 0 and 255 
xlabel('Intensity'); % Labelling the x-axis as "Intensity"
ylabel('Number of Pixels'); % Labelling the y-axis as "Number of Pixels"
%Part c
[J,K] = size(N); % Loading the enhanced image 'N' into the matrix
NoP = 1:1:256; % Y-axis values (Number of Pixels)
Int = 0:1:255; % X-axis values (Intensity)
Count = 0; % Setting an initial value
for a = 0:255 % First for loop: Checking the picture 255 times for all of the pixel values('a')
    for j = 1:J % Second for loop: Checking the pixel values row by row
        for k = 1:K % Third for loop: checking the pixel values column by column
            if N(j,k) == a % Check if the pixel value in the image matches the 'a' value
            Count = Count + 1; % If the values match the counter increments by 1
            end % Ending the if statement
        end % Ending the third for loop
    end % Ending the second for loop
    NoP(a+1) = Count; % Save the 'Count' values in an element
    Count = 0; % Clear the 'Count' so it is ready to read the next values
end % Ending the first for loop
figure(6) % New figure to display the following information
plot(Int,NoP); % Plots the intensity against the number of pixels
grid on % Displays a grid on the plot
title('Histogram of Contrast Enhanced Image'); % Labelling the title of the graph
xlim([0;255]); % Limiting the x-axis range between 0 and 255 
xlabel('Intensity'); % Labelling the x-axis as "Intensity"
ylabel('Number of Pixels'); % Labelling the y-axis as "Number of Pixels"
%%
%Question 3
G=imread('message_good.TIF');
figure()
imshow(G)
SE = [0 0 1 0];
Ge = imerode(G, SE);
figure()
imshow(Ge)
SE1 = [
    1 1 0 0 0 0 0 1 1;
    1 0 0 0 0 0 0 0 1;
    0 0 0 0 1 0 0 0 0;
    0 0 0 1 1 1 0 0 0;
    0 0 1 1 1 1 1 0 0;
    0 0 0 1 1 1 0 0 0;
    0 0 0 0 1 0 0 0 0;
    1 0 0 0 0 0 0 0 1;
    1 1 0 0 0 0 0 1 1];
Ge1 = imerode(Ge,SE1);
figure()
imshow(Ge1)
Ge2 = imerode(~Ge,~SE1);
figure()
imshow(Ge2)
Ge3 = Ge1 & Ge2;
figure()
imshow(Ge3)

% SE2 = [
%     0 0 1 1 1 1 1 0 0;
%     0 1 1 1 1 1 1 1 0;
%     1 1 1 1 0 1 1 1 1;
%     1 1 1 0 0 0 1 1 1;
%     1 1 0 0 0 0 0 1 1;
%     1 1 1 0 0 0 1 1 1;
%     1 1 1 1 0 1 1 1 1;
%     0 1 1 1 1 1 1 1 0;
%     0 0 1 1 1 1 1 0 0];
% Ge2 = imerode(G,SE2);
% figure()
% imshow(Ge2)
