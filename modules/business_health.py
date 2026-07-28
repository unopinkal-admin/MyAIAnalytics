class BusinessHealth:

    @staticmethod
    def calculate(project):

        profile = project["profile"]
        context = project["context"]

        score = 100

        strengths = []
        risks = []
        recommendations = []

        # -----------------------------
        # Data Quality
        # -----------------------------

        quality = profile["quality_score"]

        if quality >= 90:
            strengths.append("Excellent overall data quality.")
        elif quality >= 70:
            strengths.append("Good overall data quality.")
            score -= 5
        else:
            risks.append("Poor data quality.")
            recommendations.append("Improve data quality before deeper analysis.")
            score -= 20

        # -----------------------------
        # Missing Values
        # -----------------------------

        total_missing = sum(profile["missing_values"].values())

        if total_missing == 0:
            strengths.append("No missing values detected.")
        else:
            risks.append(f"{total_missing} missing values detected.")
            recommendations.append("Review and complete missing values.")
            score -= min(20, total_missing)

        # -----------------------------
        # Duplicate Records
        # -----------------------------

        duplicates = profile["duplicates"]

        if duplicates == 0:
            strengths.append("No duplicate records found.")
        else:
            risks.append(f"{duplicates} duplicate rows found.")
            recommendations.append("Remove duplicate records.")
            score -= min(15, duplicates)

        # -----------------------------
        # Numeric Columns
        # -----------------------------

        numeric_count = len(profile["numeric_columns"])

        if numeric_count > 0:
            strengths.append(
                f"{numeric_count} numeric columns available for analysis."
            )
        else:
            risks.append("No numeric columns detected.")
            recommendations.append(
                "Dataset may not support numerical analysis."
            )
            score -= 15

        # -----------------------------
        # Final Score
        # -----------------------------

        score = max(0, min(100, score))

        if score >= 90:
            status = "Excellent"
        elif score >= 75:
            status = "Good"
        elif score >= 60:
            status = "Fair"
        else:
            status = "Needs Attention"

        if not recommendations:
            recommendations.append(
                "Continue exploring the dashboard and AI insights."
            )

        return {
            "score": score,
            "status": status,
            "strengths": strengths,
            "risks": risks,
            "recommendations": recommendations,
        }
