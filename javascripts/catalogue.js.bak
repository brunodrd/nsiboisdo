
(function () {
  async function initialiserCatalogue() {
    const racine = document.getElementById("catalogue-nsi");
    if (!racine || racine.dataset.initialise === "oui") return;

    racine.dataset.initialise = "oui";

    const annee = racine.querySelector("#annee-nsi");
    const theme = racine.querySelector("#theme-nsi");
    const statut = racine.querySelector("#statut-nsi");
    const mode = racine.querySelector("#mode-nsi");
    const compteur = racine.querySelector("#compteur-nsi");
    const resultats = racine.querySelector("#resultats-nsi");

    try {
      const script = document.querySelector(
        'script[src*="javascripts/catalogue.js"]'
      );
      const url = new URL(
        "../data/catalogue_index.json",
        script.src
      );
      const reponse = await fetch(url);

      if (!reponse.ok) {
        throw new Error(`HTTP ${reponse.status}`);
      }

      const exercices = await reponse.json();

      const urlThemes = new URL(
        "../data/themes_nsi.json",
        script.src
      );
      const reponseThemes = await fetch(urlThemes);

      if (!reponseThemes.ok) {
        throw new Error(`HTTP ${reponseThemes.status} (thèmes)`);
      }

      const intitules = await reponseThemes.json();

      function nomTheme(code) {
        return intitules[code]
          ? `${intitules[code]} (${code})`
          : code;
      }

      // La page peut avoir changé pendant le chargement.
      if (!racine.isConnected) return;

      const annees = [...new Set(exercices.map(e => e.annee))]
        .sort((a, b) => b - a);

      const themes = [...new Set(exercices.flatMap(
        e => [...e.themes_dominants, ...e.themes_associes]
      ))].sort();

      annees.forEach(a => annee.add(new Option(a, a)));
      themes.forEach(t => {
        const etiquette = document.createElement("label");
        const caseTheme = document.createElement("input");

        caseTheme.type = "checkbox";
        caseTheme.value = t;

        etiquette.append(caseTheme, " " + nomTheme(t));
        theme.append(etiquette);
      });

      function afficher() {
        const themesCoches = theme.querySelectorAll(
          'input[type="checkbox"]:checked'
        );

        const resume = racine.querySelector(
          "#panneau-themes-nsi summary"
        );

        const nombre = themesCoches.length;

        resume.textContent = nombre === 0
          ? "Sélectionner les thèmes"
          : `${nombre} thème${nombre > 1 ? "s" : ""} sélectionné${nombre > 1 ? "s" : ""}`;

        const selection = exercices.filter(e => {
          if (annee.value && String(e.annee) !== annee.value)
            return false;

          const dominants = e.themes_dominants;
          const associes = e.themes_associes;

          const themesSelectionnes = Array.from(
            theme.querySelectorAll('input[type="checkbox"]:checked'),
            caseTheme => caseTheme.value
          );

          if (themesSelectionnes.length > 0) {
            const correspond = code => {
              if (statut.value === "dominant")
                return dominants.includes(code);

              if (statut.value === "associe")
                return associes.includes(code);

              return dominants.includes(code)
                  || associes.includes(code);
            };

            return mode.value === "ET"
              ? themesSelectionnes.every(correspond)
              : themesSelectionnes.some(correspond);
          }

          if (statut.value === "dominant")
            return dominants.length > 0;

          if (statut.value === "associe")
            return associes.length > 0;

          return true;
        });

        compteur.textContent = `${selection.length} exercices trouvés`;
        resultats.replaceChildren();

        selection.forEach(e => {
          const bloc = document.createElement("div");
          bloc.className = "exercice-nsi";

          const lien = document.createElement("a");
          lien.href = e.pdf;
          lien.target = "_blank";
          lien.rel = "noopener noreferrer";
          const nomFichier = e.source_pdf.split("/").pop();
          const identifiantSujet = nomFichier.replace(
            /-\d+\.pdf$/i, ""
          );

          lien.textContent =
            `${identifiantSujet.toUpperCase()} — Exercice ${e.numero}`;

          const details = document.createElement("div");
          details.className = "themes-nsi";
          details.textContent =
            `Dominants : ${e.themes_dominants.map(nomTheme).join(", ") || "—"} | ` +
            `Associés : ${e.themes_associes.map(nomTheme).join(", ") || "—"}`;

          bloc.append(lien, details);
          resultats.append(bloc);
        });
      }

      [annee, theme, statut, mode].forEach(
        element => element.addEventListener("change", afficher)
      );

      // Bouton de réinitialisation
      const boutonReset = document.createElement("button");
      boutonReset.type = "button";
      boutonReset.className = "md-button";
      boutonReset.textContent = "Réinitialiser les filtres";

      boutonReset.addEventListener("click", () => {
        annee.value = "";
        statut.value = "";
        mode.value = "ET";

        theme.querySelectorAll('input[type="checkbox"]').forEach(
          caseTheme => caseTheme.checked = false
        );

        afficher();
      });

      racine.querySelector(".filtres-nsi").after(boutonReset);

      afficher();

    } catch (erreur) {
      if (racine.isConnected) {
        compteur.textContent =
          "Erreur de chargement : " + erreur.message;
      }
    }
  }

  // Compatible avec la navigation instantanée de Material.
  if (typeof document$ !== "undefined") {
    document$.subscribe(initialiserCatalogue);
  } else {
    document.addEventListener("DOMContentLoaded", initialiserCatalogue);
  }
})();
