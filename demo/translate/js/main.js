import ru from "./ru.js"
import en from "./en.js"

const btn = document.getElementById("btn");
const output = (err, t) => {
    if (err) {
        return console.log("something went wrong loading", err);
    }
    document.getElementById("text").innerHTML = ' <i class="fa-regular fa-heart"></i> ' + t('text');
    document.getElementById("btn").innerHTML = " <i class='fa-solid fa-globe'></i> " + t("changeLang");
    document.getElementById("name").innerHTML = '<i class="fa-solid fa-user"></i> ' + t("name");
    document.getElementById("phone").innerHTML = '<i class="fa-solid fa-phone"></i> ' + t("phone");
    document.getElementById("inputName").placeholder = t("inputName");
    document.getElementById("inputPhone").placeholder = t("inputPhone");

};

i18next.init(
    {
        lng: "en",
        fallbackLng: ["en", "ru"],
        debug: true,
        resources: {
            en, ru,
        },
    },
    output
);

btn.onclick = () => {
    const lang = i18next.language === "en" ? "ru" : "en";
    i18next.changeLanguage(lang, output);
};