

    folderPath = uigetdir;
    if folderPath == 0
        disp('CANCELED');
        return;
    end


    mp4Files = dir(fullfile(folderPath, '*.mp4'));


    if isempty(mp4Files)
        disp('NO MP4');
        return;
    end

    textContent = '';
    for i = 1:length(mp4Files)
        filePath = fullfile(folderPath, mp4Files(i).name);
        if i == 1
            textContent = sprintf('adm.loadVideo("%s")\n', filePath);
        else
            textContent = [textContent sprintf('adm.appendVideo("%s")\n', filePath)];
        end
    end


    outputFilePath = fullfile(folderPath, 'video_commands.txt');
    fileID = fopen(outputFilePath, 'w');
    if fileID == -1
        disp('ERROR');
        return;
    end
    fprintf(fileID, '%s', textContent);
    fclose(fileID);

    disp(['SAVED: ' outputFilePath]);

