class ExecutiveBriefing:

    @staticmethod
    def generate(project):

        metrics = project["metrics"]
        health = project["health"]

        findings = []
        recommendations = []

        revenue = metrics.get("revenue")
        margin = metrics.get("margin")
        quality = metrics.get("quality")
        missing = metrics.get("missing")

        # -----------------------------
        # Revenue
        # -----------------------------
        if revenue is not None:
            findings.append(
                f"💰 Total Revenue: ${revenue:,.0f}"
            )

        # -----------------------------
        # Margin
        # -----------------------------
        if margin is not None:

            if margin >= 25:
                findings.append(
                    f"📈 Profit margin is strong ({margin:.1f}%)."
                )

            elif margin >= 10:
                findings.append(
                    f"📊 Profit margin is acceptable ({margin:.1f}%)."
                )

            else:
                findings.append(
                    f"⚠️ Profit margin is low ({margin:.1f}%)."
                )

                recommendations.append(
                    "Review operating costs to improve profitability."
                )

        # -----------------------------
        # Data Quality
        # -----------------------------
        if quality >= 90:

            findings.append(
                f"✅ Dataset quality is excellent ({quality:.1f}%)."
            )

        elif quality >= 70:

            findings.append(
                f"🟡 Dataset quality is good ({quality:.1f}%)."
            )

            recommendations.append(
                "Review missing records to further improve data quality."
            )

        else:

            findings.append(
                f"🔴 Dataset quality requires attention ({quality:.1f}%)."
            )

            recommendations.append(
                "Clean missing and inconsistent records."
            )

        # -----------------------------
        # Missing Values
        # -----------------------------
        if missing > 0:

            findings.append(
                f"📄 Missing values detected: {missing:,}"
            )

        # -----------------------------
        # Business Health
        # -----------------------------
        score = health.get("score", 0)

        if score >= 90:

            findings.append(
                "🟢 Overall business health is excellent."
            )

        elif score >= 75:

            findings.append(
                "🔵 Business performance is healthy."
            )

        else:

            findings.append(
                "🔴 Business performance requires attention."
            )

            recommendations.append(
                "Prioritize low-performing business areas."
            )

        # -----------------------------
        # Default Recommendation
        # -----------------------------
        if not recommendations:

            recommendations.append(
                "Continue monitoring KPIs and maintain current performance."
            )

        return {
            "findings": findings,
            "recommendations": recommendations,
        }