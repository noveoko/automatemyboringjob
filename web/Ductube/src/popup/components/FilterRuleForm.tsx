import React, { useState } from 'react';
import { FilterRule } from '../../types/FilterTypes';

interface FilterRuleFormProps {
    onSubmit: (rule: Omit<FilterRule, 'id' | 'createdAt' | 'lastModified'>) => void;
}

export const FilterRuleForm: React.FC<FilterRuleFormProps> = ({ onSubmit }) => {
    const [type, setType] = useState<FilterRule['type']>('keyword');
    const [value, setValue] = useState('');
    const [targetSite, setTargetSite] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSubmit({
            type,
            value,
            targetSite: targetSite || undefined,
            enabled: true
        });
        setValue('');
        setTargetSite('');
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-4">
            <div>
                <label className="block text-sm font-medium">Rule Type</label>
                <select
                    value={type}
                    onChange={(e) => setType(e.target.value as FilterRule['type'])}
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
                >
                    <option value="keyword">Keyword</option>
                    <option value="website">Website</option>
                    <option value="element">Element</option>
                    <option value="rating">Rating</option>
                </select>
            </div>

            <div>
                <label className="block text-sm font-medium">Value</label>
                <input
                    type="text"
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
                    required
                />
            </div>

            <div>
                <label className="block text-sm font-medium">Target Site (optional)</label>
                <input
                    type="text"
                    value={targetSite}
                    onChange={(e) => setTargetSite(e.target.value)}
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
                    placeholder="e.g., youtube.com"
                />
            </div>

            <button
                type="submit"
                className="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600"
            >
                Add Rule
            </button>
        </form>
    );
};