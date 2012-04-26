function [conditionedData]=conditionData(rawData)


test = rawData(:,2) == 0 & rawData(:,2) <= 65;
rawData(test,:) = [];

conditionedData = zeros(size(rawData));
[conditionedData(:,1), conditionedData(:,2)] = pol2cart(rawData(:,1)*pi/180, rawData(:,2));

for k=1:size(conditionedData,1);
   if conditionedData(k,1) < 0, conditionedData(k,1) = floor(conditionedData(k,1));
   elseif conditionedData(k,1) > 0, conditionedData(k,1) = ceil(conditionedData(k,1)); end
   if conditionedData(k,2) < 0, conditionedData(k,2) = floor(conditionedData(k,2));
   elseif conditionedData(k,2) > 0, conditionedData(k,2) = ceil(conditionedData(k,2)); end
end



end