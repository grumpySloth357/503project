function [data,label,num_samples] = data_load(filename)
% Function that will read txt files and load data into a cell of strings

file_id = fopen(filename);
% Counts how many number of lines are in document
fseek(file_id, 0, 'eof');
chunksize = ftell(file_id);
fseek(file_id, 0, 'bof');
ch = fread(file_id, chunksize, '*uchar');
num_samples = sum(ch == sprintf('\n')); % number of lines/samples
fclose(file_id);

% Load every line in the document and put into a cell
file_id = fopen(filename);
line = fgetl(file_id);
data = cell(num_samples,1);
data{1} = strsplit(line,',');
for i = 2:num_samples
    line = fgetl(file_id);
    data{i} = strsplit(line,','); % Split up raw data into features
end
fclose(file_id);
data = vertcat(data{:}); % Unnest cell array
% Find Labels
label = data(:,42);
% Features
data(:,42) = [];
end