def get_award_rate(supabase, award, classification, employment_type):
    result = (
        supabase.table("award_rates")
        .select("*")
        .eq("award", award)
        .eq("classification", classification)
        .eq("employment_type", employment_type)
        .eq("active", True)
        .order("effective_from", desc=True)
        .limit(1)
        .execute()
    )

    if not result.data:
        return None

    return result.data[0]
