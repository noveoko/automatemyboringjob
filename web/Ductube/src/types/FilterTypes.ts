export interface FilterRule {
    id: string;
    type: 'keyword' | 'website' | 'element' | 'rating';
    value: string;
    targetSite?: string;
    enabled: boolean;
    createdAt: number;
    lastModified: number;
}

export interface FilterSettings {
    globalEnabled: boolean;
    rules: FilterRule[];
    siteSpecificSettings: Record<string, {
        enabled: boolean;
        rules: string[];  // Rule IDs
    }>;
}
