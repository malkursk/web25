import ru from "./ru.js"
import en from "./en.js"
const output = (err, t) => {
    if (err) {
        return console.log('something went wrong loading', err);
    }
    $('#btn').html(t('changeLang'));
    $('#text').html(t('text'));
}

i18next.init({
        lng: 'en',
        fallbackLng: ["en", "ru"],
        debug: true,
        resources: {
            en,
            ru
        }
    },
    output
);

$("#btn").on("click", function () {
    const lang = i18next.language === "en" ? "ru" : "en"
    i18next.changeLanguage(lang, output);
});