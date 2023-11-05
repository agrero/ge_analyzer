import * as runelite from 'runelite';

const useragent = 'alex_laptop';

const latest = await runelite.latest({
    useragent,
});

console.log(latest)