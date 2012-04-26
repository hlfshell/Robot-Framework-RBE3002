function [  ] = frontalRadar( radarMatrix )
%FRONTALRADAR Summary of this function goes here
%   Detailed explanation goes here

output = conditionData(radarMatrix);
output = createInfraredMatrix(output);
outputFinal = filterMap(xor(output, 1) + 0);
subplot(1,2,1), imshow(output), subplot(1,2,2), imshow(outputFinal);


end

