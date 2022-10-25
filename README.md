# Does Have Bottle For Ventura?
Little Python script for checking if your current installed Homebrew formulae have bottles with support for macOS Ventura

## Motivation

With the release of macOS Ventura, I was curious to know which formulae from Homebrew already support this system, so I created this little script that checks this with JSON information from the Homebrew Formulae API

It is worth mentioning that the script only shows data from the API, since it is not yet possible to verify which bottle was used to install the formula in your case

## Usage

1. Clone the repository
```shell
git clone https://github.com/SecondThundeR/doesHaveBottleForVentura
or
npx degit SecondThundeR/doesHaveBottleForVentura
```

2. Install required packages via Poetry
```shell
poetry install
```
> If you are not using Poetry, just install asyncio and aiohttp via pip
> `pip install asyncio aiohttp`

3. Run script by passing the current list of installed formulae
```shell
brew list --formulae | python ./main.py
```

4. Check the result (Supported - highlighted in green, unsupported - in red)
<img width="1034" alt="image" src="https://user-images.githubusercontent.com/36604233/197848422-cf43fb31-56b9-4af6-bd46-607d3ffd7f63.png">

Now, if needed (for example, if you upgraded from Monterey), you can run `brew reinstall ...` and pass names of the formulae that received the upgrade

> Note: After running the script, you will get a command to reinstall the necessary formulae
> <img width="1034" alt="image" src="https://user-images.githubusercontent.com/36604233/197847620-95d88290-272b-4d00-80fe-711520b23a1d.png">
>
> It is also possible to do the same with a `brew upgrade ...`, but reinstalling seems like a pretty reliable option to me

## Credits

This library uses one external dependency: [aiohttp](https://github.com/aio-libs/aiohttp) ([License](https://github.com/aio-libs/aiohttp/blob/master/LICENSE.txt))
