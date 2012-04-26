function [ filteredMap ] = filterMap( inputMap )
%FILTERMAP Summary of this function goes here
%   Detailed explanation goes here

filteredMap = bwmorph(inputMap, 'bridge', Inf);
filteredMap = bwmorph(filteredMap, 'clean', Inf);
filteredMap = bwmorph(filteredMap, 'thicken', 5);
filteredMap = bwmorph(filteredMap, 'dilate', 3);
filteredMap = edge(filteredMap, 'canny');


end

