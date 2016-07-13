%  Parameter setting
startIndex = 1;
endIndex = 36;
imageNamePrefix = 'ANPRnum';
imageNameSuffix = '.png';
magicNumber = 2051;
numOfImage = endIndex - startIndex + 1;
numOfRows = 28;
numOfColumns = 28;
saveFileName = ['testImage',num2str(numOfImage),'.txt'];
% Process
fid = fopen(saveFileName,'wt');
% % Write magic number and other informatiion
precision = 'long';
fwrite(fid,magicNumber,precision,0,'b');
fwrite(fid,numOfImage,precision,'b');
fwrite(fid,numOfRows,precision,'b');
fwrite(fid,numOfColumns,precision,'b');
% % Write image data
for index = startIndex:1:endIndex
    imageName = [imageNamePrefix,num2str(index),imageNameSuffix];
    im = imread(imageName);
    image = imresize(im,[numOfColumns,numOfRows]);
    fwrite(fid,image,'uchar');
end

fclose(fid);
