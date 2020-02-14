function varargout = Assign2_GUI(varargin)
% ASSIGN2_GUI MATLAB code for Assign2_GUI.fig
%      ASSIGN2_GUI, by itself, creates a new ASSIGN2_GUI or raises the existing
%      singleton*.
%
%      H = ASSIGN2_GUI returns the handle to a new ASSIGN2_GUI or the handle to
%      the existing singleton*.
%
%      ASSIGN2_GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in ASSIGN2_GUI.M with the given input arguments.
%
%      ASSIGN2_GUI('Property','Value',...) creates a new ASSIGN2_GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Assign2_GUI_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Assign2_GUI_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Assign2_GUI

% Last Modified by GUIDE v2.5 15-Mar-2019 19:32:52

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Assign2_GUI_OpeningFcn, ...
                   'gui_OutputFcn',  @Assign2_GUI_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Assign2_GUI is made visible.
function Assign2_GUI_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Assign2_GUI (see VARARGIN)

% Choose default command line output for Assign2_GUI
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);


% UIWAIT makes Assign2_GUI wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Assign2_GUI_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function Enter_filename_Callback(hObject, eventdata, handles)
% hObject    handle to Enter_filename (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Enter_filename as text
%        str2double(get(hObject,'String')) returns contents of Enter_filename as a double


% --- Executes during object creation, after setting all properties.
function Enter_filename_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Enter_filename (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Browse.
function Browse_Callback(hObject, eventdata, handles)
% hObject    handle to Browse (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
disp('Load image button pressed ...')
% Create a file dialog for images
[filename, user_cancelled] = imgetfile;
if user_cancelled
    disp('User pressed cancel')
else
    disp(['User selected ', filename])
end

% Read the selected image into the variable
if filename ~= ""
    disp('Reading the image into variable X');
    X = imread(filename);
    Figure(1);imshow(X)
    %figure(Assign2_GUI);imshow(X) %display image into axes on GUI
end


% --- Executes on button press in Discontinuity.
function Discontinuity_Callback(hObject, eventdata, handles)
% hObject    handle to Discontinuity (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in Similarity.
function Similarity_Callback(hObject, eventdata, handles)
% hObject    handle to Similarity (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over Browse.
function Browse_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to Browse (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in Compare.
function Compare_Callback(hObject, eventdata, handles)
% hObject    handle to Compare (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over Discontinuity.
function Discontinuity_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to Discontinuity (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on key press with focus on Enter_filename and none of its controls.
function Enter_filename_KeyPressFcn(hObject, eventdata, handles)
% hObject    handle to Enter_filename (see GCBO)
% eventdata  structure with the following fields (see MATLAB.UI.CONTROL.UICONTROL)
%	Key: name of the key that was pressed, in lower case
%	Character: character interpretation of the key(s) that was pressed
%	Modifier: name(s) of the modifier key(s) (i.e., control, shift) pressed
% handles    structure with handles and user data (see GUIDATA)
if strcmp(eventdata.Key,'return')
    filename = hObject.String;
    if filename ~= ""
        disp('Reading the image into variable X');
        X = imread(filename);
        figure(1);imshow(X)
        %figure(Assign2_GUI);imshow(X) %display image into axes on GUI
    end
end