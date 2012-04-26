function [ infraredMatrix] = createInfraredMatrix( dataInput )
%CREATEINFRAREDMATRIX Summary of this function goes here
%   Detailed explanation goes here

%Find the size of the matrix by looking at our cartesian
%coordinates.
% tmp = sortrows(dataInput,1);
% 
% minX = abs(tmp(1,1));
% maxX = tmp(size(tmp,1), 1);
% 
% tmp = sortrows(dataInput,2);
% 
% minY = abs(tmp(1,2));
% maxY = tmp(size(tmp,1), 2);
% 
% %Ceil and floor the max and min appropiately.
% 
% if minX < 0, minX = floor(minX); else minX = ceil(minX); end
% if maxX < 0, maxX = floor(maxX); else maxX = ceil(maxX); end
% if minY < 0, minY = floor(minY); else minY = ceil(minY); end
% if maxY < 0, maxY = floor(maxY); else maxY = ceil(maxY); end

%infraredMatrix = zeros(abs(maxY) + abs(minY), abs(maxX) + abs(minX));
tmp = sortrows(abs(dataInput(:,1)));
maxX = tmp(size(tmp,1));

tmp = sortrows(abs(dataInput(:,2)));
maxY = tmp(size(tmp,1));

matrixSize = 0;

if maxX > maxY matrixSize = maxX;
else matrixSize = maxY; end

infraredMatrix = zeros(matrixSize*2);
origin = [matrixSize+1, matrixSize+1];

%Now that we have the infrared matrix, put 1's where in appropiate spot
%from the origin. The origin should be located in the last row, minX
%distance in.

%origin = [round(size(infraredMatrix,2))/2, round(size(infraredMatrix,1)/2)]
% origin = [round((abs(maxY)+abs(minY))/2), round((abs(maxX)+abs(minX))/2)]
for k=1:size(dataInput,1); infraredMatrix(dataInput(k,2) + origin(1), origin(2) - dataInput(k,1)) = 1; end
infraredMatrix = imrotate(infraredMatrix,180);
infraredMatrix = xor(infraredMatrix,1) + 0;
end

