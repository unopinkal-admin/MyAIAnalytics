class ExecutiveBriefing:

    @staticmethod
    def generate(project):

        profile = project["profile"]

        findings = []

        # Dataset size
        findings.append(
            f"Your dataset contains {profile['rows']:,} rows across {profile['columns']} columns."
        )

        # Quality
        quality = profile["quality_score"]

        if quality >= 90:
            findings.append(
                "The overall data quality is excellent."
            )
        elif quality >= 70:
            findings.append(
                "The data quality is good, but there are areas to improve."
            )
        else:
            findings.append(
                "The dataset requires cleaning before deeper analysis."
            )

        # Missing values
        missing = sum(profile["missing_values"].values())

        if missing == 0:
            findings.append(
                "No missing values were detected."
            )
        else:
            findings.append(
                f"{missing} missing values were detected."
            )

        # Duplicates
        if profile["duplicates"] == 0:
            findings.append(
                "No duplicate records were found."
            )
        else:
            findings.append(
                f"{profile['duplicates']} duplicate rows were detected."
            )

        # Recommendations
        recommendations = []

        if missing > 0:
            recommendations.append(
                "Review and resolve missing values."
            )

        if profile["duplicates"] > 0:
            recommendations.append(
                "Remove duplicate records."
            )

        recommendations.append(
            "Explore the interactive dashboard for trends."
        )

        recommendations.append(
            "Use the AI Analyst to ask business questions."
        )

        return {
            "findings": findings,
            "recommendations": recommendations
        }
