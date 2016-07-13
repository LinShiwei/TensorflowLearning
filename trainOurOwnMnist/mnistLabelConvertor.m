
% Parameter setting
magicNumber = 2049;
numOfImage = 36;
saveFileName = ['testImageLabel','.txt'];
% Process
fid = fopen(saveFileName,'wt');
precision = 'long';
fwrite(fid,magicNumber,precision,0,'b');
fwrite(fid,numOfImage,precision,'b');
% % Image label setting
labels=[5,2,3,0,3,3,3,8,6,0,6,5,6,4,9,0,7,6,3,9,0,6,8,9,0,2,8,8,2,8,2,6,6,6,6,6];
fwrite(fid,labels,'uchar');

fclose(fid);
