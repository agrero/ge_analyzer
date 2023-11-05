import * as runelite from 'runelite';
import * as FileSystem from 'fs/promises';
import * as path from 'path';

const useragent = 'alex_laptop';
const parent_dir = 'C:\\coding-projects\\ge_analyzer'
(async () => {
    const mapping = await runelite.mapping({
        useragent
    });

    console.log(mapping);

    const latest = await runelite.latest({
        useragent,
    });

    let data = JSON.stringify(latest, null, 2);

    const latestFilePath = path.join(parent_dir, 'data', 'latest.json');
    await FileSystem.writeFile(latestFilePath, data);

    let mappingData = JSON.stringify(mapping, null, 2);

    const mappingFilePath = path.join(parent_dir, 'data', 'mapping.json');
    await FileSystem.writeFile(mappingFilePath, mappingData);

})();
